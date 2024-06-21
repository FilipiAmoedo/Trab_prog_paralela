import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines

fig, ax = plt.subplots(figsize=(14, 12))
ax.axis('off')

# Define the positions of the boxes and text
positions = {
    'start': (0.5, 0.95),
    'problem_type': (0.5, 0.85),
    'data_intensive': (0.25, 0.75),
    'task_intensive': (0.75, 0.75),
    'memory_req_data': (0.25, 0.65),
    'scalability_req_task': (0.75, 0.65),
    'high_memory': (0.15, 0.55),
    'low_memory': (0.35, 0.55),
    'high_scalability': (0.65, 0.55),
    'low_scalability': (0.85, 0.55),
    'programming_ease': (0.5, 0.45),
    'easy_programming': (0.35, 0.35),
    'complex_programming': (0.65, 0.35),
    'cost_hardware': (0.5, 0.25),
    'low_cost': (0.35, 0.15),
    'high_cost': (0.65, 0.15),
    'recommendation_low': (0.35, 0.05),
    'recommendation_high': (0.65, 0.05),
}

# Draw boxes
boxes = {
    'start': mpatches.FancyBboxPatch((0.45, 0.93), 0.1, 0.04, boxstyle="round,pad=0.1", edgecolor="black"),
    'problem_type': mpatches.FancyBboxPatch((0.3, 0.83), 0.4, 0.04, boxstyle="round,pad=0.1", edgecolor="black"),
    'data_intensive': mpatches.FancyBboxPatch((0.15, 0.73), 0.2, 0.04, boxstyle="round,pad=0.1", edgecolor="black"),
    'task_intensive': mpatches.FancyBboxPatch((0.65, 0.73), 0.2, 0.04, boxstyle="round,pad=0.1", edgecolor="black"),
    'memory_req_data': mpatches.FancyBboxPatch((0.15, 0.63), 0.2, 0.04, boxstyle="round,pad=0.1", edgecolor="black"),
    'scalability_req_task': mpatches.FancyBboxPatch((0.65, 0.63), 0.2, 0.04, boxstyle="round,pad=0.1",
                                                    edgecolor="black"),
    'high_memory': mpatches.FancyBboxPatch((0.1, 0.53), 0.1, 0.04, boxstyle="round,pad=0.1", edgecolor="black"),
    'low_memory': mpatches.FancyBboxPatch((0.3, 0.53), 0.1, 0.04, boxstyle="round,pad=0.1", edgecolor="black"),
    'high_scalability': mpatches.FancyBboxPatch((0.6, 0.53), 0.1, 0.04, boxstyle="round,pad=0.1", edgecolor="black"),
    'low_scalability': mpatches.FancyBboxPatch((0.8, 0.53), 0.1, 0.04, boxstyle="round,pad=0.1", edgecolor="black"),
    'programming_ease': mpatches.FancyBboxPatch((0.4, 0.43), 0.2, 0.04, boxstyle="round,pad=0.1", edgecolor="black"),
    'easy_programming': mpatches.FancyBboxPatch((0.25, 0.33), 0.2, 0.04, boxstyle="round,pad=0.1", edgecolor="black"),
    'complex_programming': mpatches.FancyBboxPatch((0.55, 0.33), 0.2, 0.04, boxstyle="round,pad=0.1",
                                                   edgecolor="black"),
    'cost_hardware': mpatches.FancyBboxPatch((0.4, 0.23), 0.2, 0.04, boxstyle="round,pad=0.1", edgecolor="black"),
    'low_cost': mpatches.FancyBboxPatch((0.25, 0.13), 0.2, 0.04, boxstyle="round,pad=0.1", edgecolor="black"),
    'high_cost': mpatches.FancyBboxPatch((0.55, 0.13), 0.2, 0.04, boxstyle="round,pad=0.1", edgecolor="black"),
    'recommendation_low': mpatches.FancyBboxPatch((0.25, 0.03), 0.2, 0.04, boxstyle="round,pad=0.1", edgecolor="black"),
    'recommendation_high': mpatches.FancyBboxPatch((0.55, 0.03), 0.2, 0.04, boxstyle="round,pad=0.1",
                                                   edgecolor="black"),
}

for key, box in boxes.items():
    ax.add_patch(box)

# Draw text
texts = {
    'start': 'Início',
    'problem_type': 'Qual é o tipo de problema?',
    'data_intensive': 'Intensivo em Dados',
    'task_intensive': 'Intensivo em Tarefas',
    'memory_req_data': 'Qual é o requisito de memória?',
    'scalability_req_task': 'Qual é a escalabilidade necessária?',
    'high_memory': 'Alta capacidade e acesso rápido',
    'low_memory': 'Distribuição de dados entre processadores',
    'high_scalability': 'Alta escalabilidade',
    'low_scalability': 'Escalabilidade moderada',
    'programming_ease': 'É necessária alta facilidade de programação?',
    'easy_programming': 'Facilidade',
    'complex_programming': 'Complexidade',
    'cost_hardware': 'Qual é o custo e disponibilidade de hardware?',
    'low_cost': 'Baixo custo e alta disponibilidade',
    'high_cost': 'Alto custo e disponibilidade limitada',
    'recommendation_low': 'Multicores, Memória Compartilhada',
    'recommendation_high': 'Many-cores, GPUs',
}

for key, pos in positions.items():
    ax.text(pos[0], pos[1], texts[key], ha='center', va='center', fontsize=10,
            bbox=dict(facecolor='white', edgecolor='none'))

# Draw arrows
arrows = [
    ('start', 'problem_type'),
    ('problem_type', 'data_intensive'),
    ('problem_type', 'task_intensive'),
    ('data_intensive', 'memory_req_data'),
    ('task_intensive', 'scalability_req_task'),
    ('memory_req_data', 'high_memory'),
    ('memory_req_data', 'low_memory'),
    ('scalability_req_task', 'high_scalability'),
    ('scalability_req_task', 'low_scalability'),
    ('high_memory', 'programming_ease'),
    ('low_memory', 'programming_ease'),
    ('high_scalability', 'programming_ease'),
    ('low_scalability', 'programming_ease'),
    ('programming_ease', 'easy_programming'),
    ('programming_ease', 'complex_programming'),
    ('easy_programming', 'cost_hardware'),
    ('complex_programming', 'cost_hardware'),
    ('cost_hardware', 'low_cost'),
    ('cost_hardware', 'high_cost'),
    ('low_cost', 'recommendation_low'),
    ('high_cost', 'recommendation_high'),
]

for start, end in arrows:
    start_pos = positions[start]
    end_pos = positions[end]
    if start_pos[0] == end_pos[0] or start_pos[1] == end_pos[1]:
        ax.add_line(mlines.Line2D([start_pos[0], end_pos[0]], [start_pos[1], end_pos[1]], color='black', linestyle='-',
                                  linewidth=1))
    else:
        ax.add_line(
            mlines.Line2D([start_pos[0], start_pos[0]], [start_pos[1], end_pos[1]], color='black', linestyle='-',
                          linewidth=1))
        ax.add_line(mlines.Line2D([start_pos[0], end_pos[0]], [end_pos[1], end_pos[1]], color='black', linestyle='-',
                                  linewidth=1))


plt.show()
