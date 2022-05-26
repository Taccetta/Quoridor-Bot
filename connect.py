import asyncio
import json
import sys
import websockets
import time
from bot import BotQuoridor


async def start(auth_token):
    uri = "wss://4yyity02md.execute-api.us-east-1.amazonaws.com/ws?token={}".format(auth_token)
    while True:
        try:
            print('\nconnection to {}'.format(uri))
            async with websockets.connect(uri) as websocket:
                await play(websocket)
        except KeyboardInterrupt:
            print('Exiting...')
            break
        except Exception:
            print('connection error!')
            time.sleep(3)


async def send(websocket, action, data):
    message = json.dumps(
        {
            'action': action,
            'data': data,
        }
    )
    #print(message)
    await websocket.send(message)


async def play(websocket):
    while True:
        try:
            request = await websocket.recv()
            print(f"< {request}")
            request_data = json.loads(request)
            if request_data['event'] == 'update_user_list':
                pass
            if request_data['event'] == 'gameover':
                pass
            if request_data['event'] == 'challenge':
                await send(
                    websocket,
                    'accept_challenge',
                    {
                        'challenge_id': request_data['data']['challenge_id'],
                    },
                )
            if request_data['event'] == 'your_turn':
                await process_your_turn(websocket, request_data)
        except KeyboardInterrupt:
            print('Exiting...')
            break
        except Exception as e:
            print('error {}'.format(str(e)))
            break


async def process_your_turn(websocket, request_data):
        #print(request_data)
        bot_init = BotQuoridor()
        bot_init.side = request_data['data']['side']
        bot_init.board = request_data['data']['board']
        bot_init.remaining_walls = request_data['data']['walls']
        bot_init.bot_play()
        print("Remaining Walls:{}".format(bot_init.remaining_walls))
        while True:
            if bot_init.im_going_to_move == "pawn":
                await process_move(websocket, request_data, int(bot_init.final_choice[0][0]//2),
                                    int(bot_init.final_choice[0][1]//2), int(bot_init.final_choice[1][0]//2), 
                                    int(bot_init.final_choice[1][1]//2))
                del bot_init
                break
            elif bot_init.im_going_to_move == "wall":
                await process_wall(websocket, request_data, bot_init.wall_placing_coordinates[0][0]//2,
                                    bot_init.wall_placing_coordinates[0][1]//2)
                del bot_init
                break


async def process_move(websocket, request_data, from_row, from_col, to_row, to_col):
        await send(
            websocket,
            'move',
            {
                'game_id': request_data['data']['game_id'],
                'turn_token': request_data['data']['turn_token'],
                'from_row': from_row,
                'from_col': from_col,
                'to_row': to_row,
                'to_col': to_col,
            },
        )
        


async def process_wall(websocket, request_data, to_row, to_col):
    await send(
        websocket,
        'wall',
        {
            'game_id': request_data['data']['game_id'],
            'turn_token': request_data['data']['turn_token'],
            'row': to_row,
            'col': to_col,
            'orientation': 'h'
        },
    )


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        auth_token = sys.argv[1]
        asyncio.get_event_loop().run_until_complete(start(auth_token))
    else:
        print('please provide your auth_token')
