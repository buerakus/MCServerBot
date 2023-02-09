from mcstatus import JavaServer
server = JavaServer.lookup("95.216.62.170:25842")
status = server.status()
query = server.query()
listss = {', '.join(query.players.names)}
print(listss)