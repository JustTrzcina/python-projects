import time
from concurrent.futures import ProcessPoolExecutor

def ask_user():
    start = time.time()
    user_input = input("Enter your name:")
    greet = f'Hello,{user_input}'
    print(greet)
    print(f'ask_user, {time.time()-start}')

def complex_calc():
    start = time.time()
    print('Calculation started...')
    [x**2 for x in range (20000000)] 
    print(f'complex_calc, {time.time()-start}')



print(__name__)
if __name__ == "__main__":
    start= time.time()
    ask_user()
    complex_calc()
    print(f'Single thread total time: {time.time()-start}')

    start = time.time()

    with ProcessPoolExecutor(max_workers=2) as pool:
        pool.submit(complex_calc)
        pool.submit(complex_calc)

    print(f'Two processes total time: {time.time()-start}')