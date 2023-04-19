def w_sum(a, b):
    assert(len(a) == len(b))
    output = 0
    for i in range(len(a)):
        output += a[i] * b[i]
    return output


def ele_mul(number, vector):
    output = []

    for i in range(len(vector)):
        output.append(number * vector[i])

    return output


def neural_network(_input, weights):
    pred = w_sum(_input, weights)
    return pred

toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [.65, .8, .8, .9]
nfans = [1.2, 1.3, .5, 1.0]
win_or_lose_binary = [1, 1, 0, 1]
weights = [.1, .2, -1]

for i in range(4):
    _input = [toes[i], wlrec[i], nfans[i]]
    print(f'{i + 1}. {neural_network(_input, weights)}')


for i in range(len(wlrec)):
    print(f'-----{i+1}------')
    true = win_or_lose_binary[i]
    _input = [toes[i], wlrec[i], nfans[i]]


    pred = neural_network(_input, weights)
    delta = pred - true
    error = delta ** 2

    print(f'Prediction: {pred}\nError: {error}\n')

    pred = neural_network(_input, weights)

    delta = pred - true
    weight_deltas = ele_mul(delta, _input)

    alpha = 0.01

    for j in range(len(weights)):
        weights[j] -= alpha * weight_deltas[j]

    print(f'Weights: {str(weights)}\nWeight deltas: {str(weight_deltas)}\n')

    pred = neural_network(_input, weights)
    print(f'New prediction: {pred}\nError: {error}\n')
