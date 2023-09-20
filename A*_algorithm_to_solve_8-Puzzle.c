#include <stdio.h>
#include <stdlib.h>

int graph[3][3] = {{8, 3, 4}, {1, 7, 2}, {5, 6, 0}};  // Initial state
int goal_state[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 0}};  // Final state
int queue[1000][3][3];  // Queue for storing states
int n = 2;
int g = -1;

void print_graph(int graph[3][3]) {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%d ", graph[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

int up(int row_index, int col_index) {
    return row_index - 1 >= 0;
}

int down(int row_index, int col_index) {
    return row_index + 1 <= n;
}

int left(int row_index, int col_index) {
    return col_index - 1 >= 0;
}

int right(int row_index, int col_index) {
    return col_index + 1 <= n;
}

int find_row_index(int matrix[3][3], int val) {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (matrix[i][j] == val) {
                return i;
            }
        }
    }
    return -1;
}

int find_col_index(int matrix[3][3], int val) {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (matrix[i][j] == val) {
                return j;
            }
        }
    }
    return -1;
}

int find_heu(int graph[3][3]) {
    int hs = -1;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            int row = find_row_index(goal_state, graph[i][j]);
            int col = find_col_index(goal_state, graph[i][j]);
            hs += abs(row - i) + abs(col - j);
        }
    }
    return hs;
}

int find_least_hs(int queue[][3][3], int num_nodes) {
    int hs = 500;
    int g_index = -1;
    for (int i = 0; i < num_nodes; i++) {
        int current_hs = find_heu(queue[i]);
        if (current_hs <= hs) {
            hs = current_hs;
            g_index = i;
        }
    }
    printf("HS in Func: %d\n", hs);
    return g_index;
}

void copy_state(int dest[3][3], int src[3][3]) {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            dest[i][j] = src[i][j];
        }
    }
}

void create(int g) {
    int i = 0;
    copy_state(queue[i], graph);

    while (queue[0][0][0] != goal_state[0][0]) {
        printf("Level: %d\n", i);
        g++;
        int num_nodes_at_level = i + 1;
        printf("Number of nodes at each level: %d\n", num_nodes_at_level);
        int next_node_index = find_least_hs(queue, num_nodes_at_level);
        int hs = find_heu(queue[next_node_index]);
        int fs = hs + g;

        printf("H(s): %d  G(s): %d  F(s): %d\n", hs, g, fs);
        printf("\n");
        print_graph(queue[next_node_index]);

        copy_state(graph, queue[next_node_index]);
        int row_index = find_row_index(graph, 0);
        int col_index = find_col_index(graph, 0);

        if (up(row_index, col_index)) {
            int temp = graph[row_index][col_index];
            graph[row_index][col_index] = graph[row_index - 1][col_index];
            graph[row_index - 1][col_index] = temp;
            copy_state(queue[i + 1], graph);
            temp = graph[row_index][col_index];
            graph[row_index][col_index] = graph[row_index - 1][col_index];
            graph[row_index - 1][col_index] = temp;
        }

        // Implement similar logic for left, down, and right movements

        i++;
    }
}

int main() {
    create(g);
    return 0;
}
