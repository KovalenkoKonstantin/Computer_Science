import time

stat = time.time()
for i in range(1, 60000):
    print(i)
end = time.time()
print(end - stat)
