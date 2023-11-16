import matplotlib.pyplot as plt
import random

class EdgeTriggeredSRFlipFlop:
    def _init_(self):
        self.Q = 0  
        self.Q_bar = 1  

    def set(self, S, R, CLK, PR, CLR):
        if PR:
            self.Q = 1  
            self.Q_bar = 0
        elif CLR:
            self.Q = 0  
            self.Q_bar = 1
        elif CLK:
            if S and not R:
                self.Q = 1  
                self.Q_bar = 0
            elif R and not S:
                self.Q = 0  
                self.Q_bar = 1

    def get_output(self):
        return self.Q, self.Q_bar


def simulate_flip_flop(num_clock_cycles):
    flip_flop = EdgeTriggeredSRFlipFlop()
    q_values, q_bar_values = [], []

    for _ in range(num_clock_cycles):
        S = random.choice([0, 1])
        R = random.choice([0, 1])
        CLK = random.choice([0, 1])
        PR = random.choice([0, 1])
        CLR = random.choice([0, 1])

        flip_flop.set(S, R, CLK, PR, CLR)
        q, q_bar = flip_flop.get_output()
        q_values.append(q)
        q_bar_values.append(q_bar)

    return q_values, q_bar_values


num_clock_cycles = 20

q_values, q_bar_values = simulate_flip_flop(num_clock_cycles)


time = [i for i in range(num_clock_cycles)]


plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.step(time, q_values, where='post', label='Q', color='blue')
plt.ylabel('Q Output Value')
plt.title('Negative Edge-Triggered SR Flip-Flop Q and Q\' Waveforms')
plt.legend(loc='upper left')
plt.grid(True)


plt.subplot(2, 1, 2)
plt.step(time, q_bar_values, where='post', label="Q'", color='red')
plt.xlabel('Time (Clock Cycles)')
plt.ylabel("Q' Output Value")
plt.legend(loc='upper left')
plt.grid(True)

plt.tight_layout()

plt.show()