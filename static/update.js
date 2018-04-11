var chatSocket = new WebSocket(
        'ws://' + window.location.host +
        '/clicks/');
     chatSocket.onmessage = function(e) {
        var data = JSON.parse(e.data);
        var message = data['message'];
        document.querySelector('#click-count').value = "Clicks: " + message;
    };
    chatSocket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    };

document.querySelector('#clicker').onclick = function(e) {
    chatSocket.send(JSON.stringify({
        'addAmount': 1
    }));
};