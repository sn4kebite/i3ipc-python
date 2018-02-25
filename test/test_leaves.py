from ipctest import IpcTest
import i3ipc

class TestLeaves(IpcTest):

    def test_workspace_leaves(self, i3):
        ws_name = self.fresh_workspace()
        con1 = self.open_window()
        command = i3.command('[id=%s] floating enable' % con1)
        con2 = self.open_window()
        con3 = self.open_window()

        ws = next(filter(lambda w: w.name == ws_name,
            i3.get_tree().workspaces()))
        assert(len(ws.leaves()) == 3)