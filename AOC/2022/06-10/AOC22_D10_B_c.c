#include <stdio.h>
#include <string.h>

int update_cell(char arr[6][40], int cycle, int reg_val)
{
    int col = (cycle - 1) % 40;
    if (col - 1 <= reg_val && reg_val <= col + 1)
    {
        arr[(cycle - 1) / 40][col] = '#';
    }
}

int main(int argc, char *argv[])
{
    char line[10], arr[6][40];
    int cycle, result = 0;
    int reg_val = 1;

    // Create Array
    for (int i = 0; i < 6; i++)
    {
        for (int j = 0; j < 40; j++)
        {
            arr[i][j] = '.';
        }
    }

    // Get Input
    FILE *file = fopen(argv[1], "r");
    while (fgets(line, 10, file) != NULL)
    {
        cycle++;
        update_cell(arr, cycle, reg_val);
        if (line[0] == 'a')
        {
            cycle++;
            update_cell(arr, cycle, reg_val);

            // String to int
            int sign = 1;
            int val = 0;
            for (int i = 5; i < strlen(line); i++)
            {
                if (line[i] - '0' == -3)
                {
                    sign = -1;
                }
                if ('0' <= line[i] && line[i] <= '9')
                {
                    val = val * 10 + (line[i] - '0') * sign;
                }
            }
            reg_val += val;
        }
    }
    fclose(file);

    // Print Final Matrix
    for (int i = 0; i < 6; i++)
    {
        for (int j = 0; j < 40; j++)
        {
            printf("%c", arr[i][j]);
        }
        printf("\n");
    }
    return 0;
}
