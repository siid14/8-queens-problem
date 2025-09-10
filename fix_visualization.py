#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

# Create fixed visualization for Run 3
fig, ax = plt.subplots(figsize=(10, 6))

# Data for Run 3 - solution found immediately (only 1 data point)
generations = [0]
best_fitness = [0]
avg_fitness = [5.2]

# Plot points instead of lines for single data point
ax.plot(generations, best_fitness, 'bo', label='Best Fitness', markersize=12, 
        markeredgecolor='darkblue', markeredgewidth=2)
ax.plot(generations, avg_fitness, 'ro', label='Average Fitness', markersize=12, 
        markeredgecolor='darkred', markeredgewidth=2)

# Set proper axis limits
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-0.5, 6)
ax.set_xticks([0])
ax.set_yticks(range(7))

# Add explanatory text
ax.text(0, 5.5, 'Solution found in initial population!\nBest: 0, Avg: 5.2', 
        ha='center', va='bottom', fontsize=12, 
        bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', alpha=0.8))

ax.set_xlabel('Generation')
ax.set_ylabel('Fitness (Number of Attacking Pairs)')
ax.set_title('Fitness Evolution - Run 3 pm=100.0% (Fixed)')
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('fitness_evolution_Run_3_FIXED.png', dpi=150, bbox_inches='tight')
plt.close()

print("Fixed visualization created: fitness_evolution_Run_3_FIXED.png")
print("\nEXPLANATION:")
print("- Run 3 with 100% mutation found a solution in the initial population")
print("- This means only 1 data point exists (generation 0)")
print("- A line graph with 1 point appears empty")
print("- The fixed version shows the single point as circles with explanatory text")
