def serialize(R, res):
    def fun(R):
        if R:
            res.append(str(R.data))
            fun(R.left)
            fun(R.right)
        else:
            res.append('#')
    fun(R)
    return res

def deSerialize(data):
    i = [0]

    def fun():
        val = data[i[0]]
        i[0]+=1
        if val == '#':
            return None
        
        R = Node(int(val))
        R.left = fun()
        R.right = fun()
        return R
    
    return fun()
