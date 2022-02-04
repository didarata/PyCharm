pool_volume = int(input())
flow_rate_first_pipe = int(input())
flow_rate_second_pipe = int(input())
worker_missing = float(input())

first_pipe_volume = flow_rate_first_pipe * worker_missing
second_pipe_volume = flow_rate_second_pipe * worker_missing
both_pipe_volume = first_pipe_volume + second_pipe_volume
total_pool_volume = both_pipe_volume - pool_volume

first_pipe_percentage = (first_pipe_volume / both_pipe_volume) * 100
second_pipe_percentage = (second_pipe_volume / both_pipe_volume) * 100
pool_volume_percentage = (both_pipe_volume / pool_volume) * 100

if pool_volume >= both_pipe_volume:
    print(f'The pool is {pool_volume_percentage:.2f}% full. Pipe 1: {first_pipe_percentage:.2f}%. Pipe 2: {second_pipe_percentage:.2f}%.')
else:
    print(f'For {worker_missing} hours the pool overflows with {total_pool_volume:.2f} liters.')