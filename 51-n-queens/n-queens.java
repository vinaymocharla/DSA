class Solution {
    Set<Integer> cols = new HashSet();
    Set<Integer> posDiag = new HashSet();
    Set<Integer> negDiag = new HashSet();
    List<List<String>> result = new ArrayList();
    public List<List<String>> solveNQueens(int n) {

        char[][] board = new char [n][n];


        for(int i=0;i<n;i++){
            for (int j=0;j<n;j++){

                board[i][j]='.';
            }
        }

        backtrack(0,board,n);
        return result;
        
    }

    public void backtrack(int r, char[][] board,int n  ){

        List<String> copy = new ArrayList();
        if(r==n){

            for(char[] row:board){

                copy.add(new String(row));
            }

            result.add(copy);
            return;

        }

        for(int c=0;c<n;c++){

            if(cols.contains(c) || posDiag.contains(r+c) || negDiag.contains(r-c)){

                continue;
            }

            cols.add(c);
            posDiag.add(r+c);
            negDiag.add(r-c);

            board[r][c] = 'Q';

            backtrack(r+1,board,n );

            cols.remove(c);
            posDiag.remove(r+c);
            negDiag.remove(r-c);
            board[r][c] = '.';

        }


    }
}