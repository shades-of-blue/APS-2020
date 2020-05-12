#include<bits/stdc++.h>
using namespace std;

int main()
{
    int M,N,count=0;
    cin>>M>>N;
    int matrix[M][N];
    
    for(int i=0;i<M;i++)
    {
        for(int j=0;j<N;j++)
        {
            scanf("%d",&matrix[i][j]);
            if(matrix[i][j]<0)
                count++;
        }
    }

    int S[M+1][N+1];
    
    for (int i = 0; i <= M; i++)
    {
        for (int j = 0; j <= N; j++)
        {
            if (i == 0 || j == 0)
                S[i][j] = 0;
            else
                S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] +
                        matrix[i-1][j-1];
        }
    }

    int maxSum = INT_MIN;
    int rowStart, rowEnd, colStart, colEnd;


    for (int i = 0; i < M; i++)
    {
        for (int j = i; j < M; j++)
        {
            for (int m = 0; m < N; m++)
            {
                for (int n = m; n < N; n++)
                {
                    int submatrix_sum = S[j+1][n+1] - S[j+1][m] - 
                                    S[i][n+1] + S[i][m];

                    if (submatrix_sum > maxSum)
                    {
                        maxSum = submatrix_sum;
                        rowStart = i;
                        rowEnd = j;
                        colStart = m;
                        colEnd = n;
                    }
                }
            }
        }
    }

    cout<<maxSum<<endl;

    for(int i=rowStart;i<=rowEnd;i++){
        for(int j=colStart;j<=colEnd;j++)
        if(matrix[i][j]<0){
            maxSum=maxSum - 2*matrix[i][j] + matrix[i][j];
        }
    }

    cout<<maxSum<<endl;

    return 0;
}