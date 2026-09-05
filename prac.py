def hello_db():
    try:
        color = "blue"
        for i in range(5):
            yield color[i]
    finally:
        print("madhara uchiha")


ans = hello_db()
print(next(ans) + " madhara")
print(next(ans))
