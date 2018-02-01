function setFEN(table, fen) {
    var arr = (fen || DefaultFen).split(" ")[0].split("/");
    for (var rank = 0; rank < 8; rank++) {
        var file = 0;
        for (var j = 0, len = arr[rank].length; j < len; j++) {
            var char = arr[rank].charAt(j);
            if (isNaN(+char)) {
                var piece = char.toLowerCase();
                var white = (char != piece);
                // ChessBoard[rank][file] = (piecesNames.indexOf(piece) + 1) * (white ? 1 : -1);

                var cell = table.rows[rank].cells[file];
                cell.innerHTML = pieces[piece][white ? 0 : 1];
                cell.className = (white ? 'w' : 'b') + piece;
                file++;
            } else {
                file += +char;
            }
        }
    }
}

/*
var ChessBoard = new Array(8);
for (var I = 8; I--;) {
    ChessBoard[I] = new Array(8);
}
var piecesNames = "pnbrqk";
*/

var pieces = {
    'k': ['\u2654', '\u265A'],
    'q': ['\u2655', '\u265B'],
    'r': ['\u2656', '\u265C'],
    'b': ['\u2657', '\u265D'],
    'n': ['\u2658', '\u265E'],
    'p': ['\u2659', '\u265F']
};

var DefaultFen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq -";

$(function() {
    setFEN($('#chessboard')[0], "5Rk1/1b2p2p/p2pP1p1/2rP4/2BQ2P1/6qP/PP6/1K6 b - -");
});
