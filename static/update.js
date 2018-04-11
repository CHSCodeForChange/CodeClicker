var chatSocket = new WebSocket(
        'ws://coding-clicker.herokuapp.com/clicks');
     chatSocket.onmessage = function(e) {
        var data = JSON.parse(e.data);
        var message = data['clicks'];
        document.querySelector('#click-count').value = "Clicks: " + message;
    };
    chatSocket.onclose = function(e) {
        console.error('Socket closed unexpectedly');
    };

document.querySelector('#clicker').onclick = function(e) {
    console.info('testing')
    chatSocket.send(JSON.stringify({
        'addAmount': 1
    }));
};