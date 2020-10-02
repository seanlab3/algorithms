from algorithms.dp import schedule,Job

# star,finish,profit

job = [Job(1, 2, 50), Job(3, 5, 20),
       Job(6, 19, 100), Job(2, 100, 200)]

print(schedule(job))

# 박제준 6/18