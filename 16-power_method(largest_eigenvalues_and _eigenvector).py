import numpy as np

a = np.array([[3, 0, 1],
              [2, 2, 2],
              [4, 2, 5]])

x = np.array([[1], [1], [1]])
tolerable_error = 0.01
max_iteration = 10

lambda_old = 1.0
condition = True
step = 1
while condition:
    x = np.matmul(a, x)
    lambda_new = max(abs(x))

    x = x / lambda_new
    print('\nSTEP %d' % (step))
    print('----------')
    print('Eigen Value = %0.4f' % (lambda_new))
    print('Eigen Vector: ')
    for i in range(a.shape[0]):
        print('%0.3f\t' % (x[i]))

    step = step + 1
    if step > max_iteration:
        print('Not convergent in given maximum iteration!')
        break

    error = abs(lambda_new - lambda_old)
    print('error=' + str(error))
    lambda_old = lambda_new
    condition = error > tolerable_error
