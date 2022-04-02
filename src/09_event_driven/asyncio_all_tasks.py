import asyncio


async def task():
    print('task')


async def main():
    # await asyncio.sleep(1)
    print('main task:', asyncio.current_task())

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        task1 = loop.create_task(task())
        task2 = loop.create_task(task())
        task3 = loop.create_task(task())

        pending = asyncio.all_tasks(loop)
        print(pending)

        print(task1)
        print(task2)
        print(task3)

        task3.cancel()

        print(task3)

        loop.run_until_complete(main())
    except Exception as e:
        print(e)
    finally:
        loop.close()


'''
{
    <Task pending name='Task-3' coro=<task() running at asyncio_all_tasks.py:4>>, 
    <Task pending name='Task-2' coro=<task() running at asyncio_all_tasks.py:4>>, 
    <Task pending name='Task-1' coro=<task() running at asyncio_all_tasks.py:4>>
}

<Task pending name='Task-1' coro=<task() running at asyncio_all_tasks.py:4>>
<Task pending name='Task-2' coro=<task() running at asyncio_all_tasks.py:4>>
<Task pending name='Task-3' coro=<task() running at asyncio_all_tasks.py:4>>
<Task cancelling name='Task-3' coro=<task() running at asyncio_all_tasks.py:4>>

task
task

main task: <Task pending name='Task-4' coro=<main() running at asyncio_all_tasks.py:10> 
                 cb=[_run_until_complete_cb() at python3.9/asyncio/base_events.py:184]>
'''
