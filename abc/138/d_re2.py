max_n = 100100
g = [0] * max_n
begin = [0] * 2 * max_n
end = [0] * 2 * max_n
k = 0
root = 0

euler_tour = []

def dfs(v, p):
    begin[v] = k
    euler_tour.append(v)
    k += 1
    for i in g[v]:


dfs(root, -1)

# #include <vector>
# using namespace std
# #define pb push_back
# #define MAX_N 100100
# vector < int > g[MAX_N]
# vector < int > euler_tour
# int begin[2*MAX_N], end[2*MAX_N]
# int k = 0, root = 0
# void dfs(int v, int p)
# {
#     begin[v] = k
#     euler_tour.pb(v)
#     k++
#     for(int i=0
#         i < g[v].size()
#         i++)
#     {
#         if(g[v][i] != p)
#         {
#             dfs(g[v][i], v)
#             euler_tour.pb(v)
#             k++
#         }
#     }
#     end[v] = k
# }
# int main()
# {
#     dfs(root, -1)
# }
