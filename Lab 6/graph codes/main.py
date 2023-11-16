import random
import matplotlib.pyplot as plt

def sr_latch(s, r, state):
    if s == 1 and r == 0:
        return 1, 0  
    elif s == 0 and r == 1:
        return 0, 1  
    else:
        return state, 1 - state  

state = 0  
iterations = 50  

time_steps = [0]
Q_values = [state]
Q_not_values = [1 - state]
last_s, last_r = 0, 0

for _ in range(iterations):
    s = random.randint(0, 1)
    r = random.randint(0, 1)

    if s != last_s or r != last_r:
        time_steps.append(time_steps[-1] + 1)
        state, state_not = sr_latch(s, r, state)
        Q_values.append(state)
        Q_not_values.append(state_not)

    last_s, last_r = s, r


plt.figure(figsize=(12, 8))


plt.subplot(2, 1, 1)
plt.step(time_steps, Q_values, where='post', label='Q', color='blue')
plt.ylabel('Q Output Value')
plt.title('Active HIGH S-R Latch Waveform with Input Changes')
plt.legend(loc='upper left')
plt.grid(True)


plt.subplot(2, 1, 2)
plt.step(time_steps, Q_not_values, where='post', label="Q'", color='red')
plt.xlabel('Time (Clock Cycles)')
plt.ylabel("Q' Output Value")
plt.legend(loc='upper left')
plt.grid(True)

plt.tight_layout()

plt.show()