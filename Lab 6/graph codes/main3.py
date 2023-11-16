import matplotlib.pyplot as plt

numCycles = int(input('Enter the number of clock cycles to simulate: '))

clockSignal = [0] * numCycles
presetSignal = [0] * numCycles
clearSignal = [0] * numCycles
J = [0] * numCycles
K = [0] * numCycles
Q = [0] * numCycles
Q_bar = [0] * numCycles

for cycle in range(numCycles):
    clockSignal[cycle] = cycle % 2

    print(f'Enter input values for clock cycle {cycle}:')
    J[cycle] = int(input('Enter the value for J (1 for active HIGH, 0 for inactive): '))
    K[cycle] = int(input('Enter the value for K (1 for active HIGH, 0 for inactive): '))
    presetSignal[cycle] = int(input('Enter the value for CLEAR (CLR) (1 for active LOW, 0 for inactive): '))
    clearSignal[cycle] = int(input('Enter the value for PRESET (PR) (1 for active LOW, 0 for inactive): '))

    if cycle > 0:
        if clockSignal[cycle] == 1 and clockSignal[cycle - 1] == 0:
            if clearSignal[cycle] == 0 and presetSignal[cycle] == 0:
                if J[cycle] == 0 and K[cycle] == 0:
                    Q[cycle] = Q[cycle - 1]  
                elif J[cycle] == 0 and K[cycle] == 1:
                    Q[cycle] = 0  
                elif J[cycle] == 1 and K[cycle] == 0:
                    Q[cycle] = 1  
                elif J[cycle] == 1 and K[cycle] == 1:
                    Q[cycle] = 1 - Q[cycle - 1]  
            else:
                Q[cycle] = Q[cycle - 1] 
        else:

            Q[cycle] = Q[cycle - 1]
    else:
        if J[cycle] == 0 and K[cycle] == 0:
            Q[cycle] = 0
        elif J[cycle] == 0 and K[cycle] == 1:
            Q[cycle] = 0
        elif J[cycle] == 1 and K[cycle] == 0:
            Q[cycle] = 1
        elif J[cycle] == 1 and K[cycle] == 1:
            Q[cycle] = 1
    Q_bar[cycle] = 1 - Q[cycle]

time = list(range(1, numCycles + 1))

plt.figure()
plt.step(time, clockSignal, where='post', color='red', label='Clock')
plt.step(time, clearSignal, where='post', color='green', label='CLEAR (CLR)')
plt.step(time, presetSignal, where='post', color='blue', label='PRESET (PR)')
plt.step(time, J, where='post', color='magenta', label='J (Input)')
plt.step(time, K, where='post', color='cyan', label='K (Input)')
plt.step(time, Q, where='post', color='black', label='Q (Output)')
plt.step(time, Q_bar, where='post', color='yellow', label='Q_bar (Output)')

plt.title('Flip-Flop Inputs and Outputs')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend(loc='best')

plt.show()
