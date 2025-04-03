#include <iostream>
#include <deque>
#include <vector>
#include <unordered_map>

using namespace std;

int main() {
    int n, N, q;
    cin >> n >> N >> q;
    vector<deque<int>> dq(N);
    unordered_map<int, bool> st;  // 是否存在缓存中
    unordered_map<int, bool> r;   // 是否被修改过（脏）

    for (int i = 0; i < q; ++i) {
        int op, a;
        cin >> op >> a;

        int group = (a / n) % N;  // 计算组号

        if (st.count(a) && st[a]) {  // 命中
            // 找到该元素并移动到前端
            auto& deq = dq[group];
            for (auto it = deq.begin(); it != deq.end(); ++it) {
                if (*it == a) {
                    deq.erase(it);
                    deq.push_front(a);
                    break;
                }
            }
            // 如果是写操作，标记为脏
            if (op == 1) {
                r[a] = true;
            }
        } else {  // 未命中
            // 需要载入数据，可能替换
            if (dq[group].size() >= n) {  // 需要替换
                int victim = dq[group].back();
                dq[group].pop_back();
                st[victim] = false;
                if (r.count(victim) && r[victim]) {
                    cout << "1 " << victim << endl;
                    r.erase(victim);
                }
            }
            // 载入新数据
            dq[group].push_front(a);
            st[a] = true;
            if (op == 1) {
                r[a] = true;
            } else {
                r[a] = false;  // 读操作，未被修改
            }
            // 输出读内存操作
            cout << "0 " << a << endl;
        }
    }
    return 0;
}
