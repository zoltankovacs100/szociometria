from flask import Flask, jsonify
import networkx as nx

# Flask alkalmazás létrehozása
app = Flask(__name__)

# Egy egyszerű példa gráf létrehozása a networkx segítségével
G = nx.Graph()
G.add_edges_from([
    ("A", "B"), ("A", "C"),
    ("B", "D"), ("B", "E"),
    ("C", "F"),
    ("E", "F")
])

# Definiálunk egy API végpontot
@app.route('/shortest_path/<start_node>/<end_node>')
def shortest_path(start_node, end_node):
    """
    Ez a funkció megkeresi a legrövidebb utat a start_node és end_node között.
    """
    try:
        # A networkx segítségével kiszámoljuk a legrövidebb utat
        path = nx.shortest_path(G, source=start_node, target=end_node)
        # Az eredményt JSON formátumban adjuk vissza
        return jsonify({
            "start_node": start_node,
            "end_node": end_node,
            "shortest_path": path
        })
    except nx.NetworkXNoPath:
        # Ha nincs út a két pont között
        return jsonify({"error": f"No path found between {start_node} and {end_node}"}), 404
    except nx.NodeNotFound as e:
        # Ha a megadott pont nem létezik a gráfban
        return jsonify({"error": str(e)}), 404

# Az alkalmazás futtatása, ha ezt a fájlt direkt indítjuk
if __name__ == '__main__':
    # A 0.0.0.0 host biztosítja, hogy a szerver a hálózaton is elérhető legyen
    app.run(host='0.0.0.0', port=5000, debug=True)
