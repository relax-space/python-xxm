import traceback

def zero():
    try:
        a = 0
        b = 1
        c =b/a
        return None
    except Exception as inst:
        return traceback.format_exc()

err = zero()
print(err)