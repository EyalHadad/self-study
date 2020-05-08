def solution(src, dest):
    class Board(object):
        def __init__(self,b_src,b_dst):
            self.src = Node(b_src,0)
            self.dst = Node(b_dst,0)
            self.count_move = 0
            self.node_dict = {self.src.pos: self.src, self.dst.pos: self.dst}
            self.open_list = [self.src]

        def solve(self):
            while self.open_list:
                self.get_neighbors(self.open_list[0])
                self.count_move += 1
                pop_res = self.open_list.pop(0)
                if pop_res.pos == self.dst.pos:
                    return self.dst.distanse
                pop_res.visited = True

            return -1

        def get_neighbors(self, node):
            x_pos = int(node.pos / 8)
            y_pos = int(node.pos % 8)
            double = lambda p: x_pos + p[0] < 8 and y_pos + p[1] < 8 and x_pos + p[0] >= 0 and y_pos + p[1] >= 0
            pos_list = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
            filterd_list = filter(double,pos_list)
            self.update_nodes([(x_pos + p[0] )* 8 + p[1] + y_pos for p in filterd_list],node.distanse)

        def update_nodes(self, nodes_ind, dist):
            for ind in nodes_ind:
                if ind not in self.node_dict:
                    new_node = Node(ind, dist +1)
                    self.node_dict[ind] = new_node
                    self.open_list.append(new_node)
                else:
                    if not self.node_dict[ind].visited:
                        self.node_dict[ind].distanse = dist +1
                        self.open_list.append(self.node_dict[ind])

    class Node(object):
        def __init__(self, position, dist):
            self.visited = False
            self.pos = position
            self.distanse = dist

    b = Board(src, dest)
    return b.solve()