class LRUCache {
public:
    LRUCache(int capacity) : capacity(capacity) {
        left = new Node();
        right = new Node();
        left->next = right;
        right->prev = left;
    }
    
    int get(int key) {
        auto it = cache.find(key);
        if (it == cache.end()) return -1;
        del(it->second);
        ins(it->second);
        return (it->second->val);
    }
    
    void put(int key, int value) {
        auto it = cache.find(key);
        if (it != cache.end()){
            del(it->second);
            delete it->second;
        }
        cache[key] = new Node(key, value);
        ins(cache[key]);

        if (int(cache.size()) > capacity){
            Node* t = left->next;
            del(t);
            cache.erase(t->key);
            delete t;
        }
    }

private:
struct Node{
    int key, val;
    Node *prev, *next;
    Node(int k = 0, int v = 0) : key(k), val(v), prev(nullptr), next(nullptr) {}
};

int capacity;
unordered_map<int, Node*> cache;
Node *left, *right;

void ins(Node* node){
    node->next = right;
    node->prev = right->prev;
    node->prev->next = node;
    right->prev = node;
}

void del(Node* node){
    node->prev->next = node->next;
    node->next->prev = node->prev;
}

};
