function isValidSudoku(board: string[][]): boolean {
    

    const set = new Set()

    for(let i=0;i<9;i++){
        for(let j=0;j<9;j++){

            const cell = board[i][j]

            if(cell==='.') continue

            const row=`${cell} is present in row ${i}`
            const column=`${cell} is present in column ${j}`
            const box=`${cell} is present in block ${Math.floor(i/3)} - ${Math.floor(j/3)}`

            if(set.has(row) || set.has(column) || set.has(box)) return false

            set.add(row).add(column).add(box)

        


        }
    }

    return true
};