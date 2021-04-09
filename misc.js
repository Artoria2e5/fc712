
// nth row of the pascal triangle
const binom_row = function(n) {
    let row = [1, 1];
    for (let i = 1; i < n; i++) {
        let newrow = [1];
        for (let j = 1; j <= row.length; j++) {
            newrow[j] = (row[j] || 0) + row[j - 1];
        }
        row = newrow;
    }
    return row;
}
