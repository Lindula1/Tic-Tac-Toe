import tkinter
import customtkinter as CTK
import tkinter.font as Font

class TTT(CTK.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Tic-Tac-Toe")
        self.def_gmty = "480x660"
        self.geometry(self.def_gmty)
        self.top_frame = CTK.CTkFrame(self, fg_color="transparent", corner_radius=0, border_width=0)
        self.top_frame.pack(side="top", fill="both", expand=True)
        self.scoreboard = CTK.CTkFrame(self.top_frame, fg_color="transparent", corner_radius=0, border_width=2)
        self.scoreboard.pack(side="top", fill="x", expand=True, pady=12)
        self.bottom_frame = CTK.CTkFrame(self, fg_color="transparent", corner_radius=0, border_width=0)
        self.bottom_frame.pack(side="bottom", fill="both", expand=True)
        #self.hotbar = CTK.CTkFrame(self.top_frame, fg_color="transparent", corner_radius=0, border_width=0)
        #self.hotbar.pack(side="top", fill="x")
        self.p1_score = self.p2_score = 0
        self.display_grid = [[None for x in range(3)] for x in range(3)]
        self.grid = [[8 for x in range(3)] for x in range(3)]
        self.current_p = 0
        self.Map_Scoreboard()
        self.Map_Game_View(self.bottom_frame)
    
    def Map_Scoreboard(self):
        font = CTK.CTkFont(family="Arial Black", size=78, weight=Font.NORMAL)
        self.p1_score_lbl = CTK.CTkLabel(self.scoreboard, fg_color="gray23",font=font, text=self.p1_score, text_color="skyblue")
        self.p1_score_lbl.pack(side="left", padx=60, pady=2, ipadx=65)
        self.p2_score_lbl = CTK.CTkLabel(self.scoreboard, fg_color="gray23",font=font, text=self.p2_score, text_color="slateblue")
        self.p2_score_lbl.pack(side="right", padx=60, pady=2, ipadx=65)
    
    def Current_Player(self):
        if self.current_p == 0:
            self.current_p = 1
        else:
            self.current_p = 0
    
    def Map_Game_View(self, master):
        font = CTK.CTkFont(family="Arial Black", size=70, weight=Font.NORMAL)
        for row in range(3):
            frame = CTK.CTkFrame(master, fg_color="transparent")
            frame.pack(side="top", expand=True, anchor="n")
            for column in range(3):
                btn = CTK.CTkButton(frame, width=118, height=30, font=font, text=" ", command=lambda: self.Select(row, column), border_width=8, border_color="grey87")
                btn.pack(side="left", padx=18, pady=8)
                self.display_grid[row][column] = btn
        for b in self.display_grid:
            for box in b:
                box.configure(state="normal", text=" ")

    def Unpack_Children(self, parent):
        for widget in parent.winfo_children():
            if widget.winfo_ismapped():
                widget.pack_forget()

    def Select(self, row, col):
        self.grid[row][col] = self.current_p
        self.Change_Box(row, col)
        self.Current_Player()
        self.Winning_Condition()
    
    def Change_Box(self, row, col):
        if self.current_p == 0:
            self.display_grid[row][col].configure(text="O")
        else:
            self.display_grid[row][col].configure(text="X")
    
    def Winning_Condition(self):
        # Row winning logic
        for row in self.grid:
            if sum(row) == 3:
                print("x wins via row")
            elif sum(row) == 0:
                print("o wins via row")
        
        # Column winning logic
        for i in range(3):
            column = [row[i] for row in self.grid]
            if sum(column) == 3:
                print("x wins via column")
            elif sum(column) == 0:
                print("o wins via column")
        
        # Diagonal winning logic
        neg_diag = pos_diag = 0
        for i in range(3):
            neg_diag += self.grid[i][i]
            pos_diag += self.grid[i][2-i]
        if pos_diag == 3 or neg_diag == 3:
            print("x wins via diagonal")
        elif pos_diag == 0 or neg_diag == 0:
            print("o wins via diagonal")

if __name__ == "__main__":
    game = TTT()
    game.resizable(False,False)
    game.mainloop()