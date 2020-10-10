function FindProxyForURL(url, host) {
    if (host == 'music.163.com' || host == 'interface.music.163.com' || host == 'interface3.music.163.com' || host == 'apm.music.163.com' || host == 'apm3.music.163.com' || host == '59.111.181.38' || host == '59.111.181.60' || host == '223.252.199.66' || host == '223.252.199.67' || host == '59.111.160.195' || host == '59.111.160.197' || host == '193.112.159.225' || host == '39.105.63.80' || host == '47.100.127.239' || host == '118.24.63.156' || host == '59.111.181.35'|| host == '115.236.118.33'|| host == '115.236.121.1'|| host == '112.13.122.1'|| host == '112.13.119.17'|| host == '103.126.92.132') {
        return 'PROXY 106.14.119.104:1553;'
    }
   if (isInNet(host, "10.0.0.0",  "255.0.0.0")){
     return "DIRECT";
   }
   if (shExpMatch(url, "*zju*")){
     return "DIRECT";
   }
    return 'PROXY zju.wenzhub.top:7890;PROXY 106.14.119.104:7004;SOCKS5 106.14.119:7004;DIRECT;'
}
