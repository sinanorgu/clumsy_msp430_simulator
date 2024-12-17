import pygame,sys
import entry
import button
import text
import execute_op
import ss_display
pygame.init()
#pencere = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pencere = pygame.display.set_mode((1400,800))


stack = []
memory = []

registers = {}

registers['r1'] = 0
registers['r2'] = 0
registers['r3'] = 0
registers['r4'] = 0
registers['r5'] = 0
registers['r6'] = 0
registers['r7'] = 0
registers['r8'] = 0
registers['r9'] = 0
registers['r10'] = 0
registers['r11'] = 0
registers['r12'] = 0
registers['r14'] = 0
registers['r15'] = 0

registers['pc'] = 0
registers['&p2in'] = 0
registers['&p1in'] = 0
registers['&p1dir'] = 0
registers['&p2dir'] = 0
registers['&p1out'] = 0
registers['&p2out'] = 0




registers["flag_z"] = 0
registers["flag_n"] = 0


def get_code_line_buttons():
    global code_line_buttons
    code_line_buttons = []
        
    for i in range(len(code_lines)) :
        satir = button.button( " ".join(code_lines[i]),600,i*25+(bias1+bias2),250,25)
        satir.on_mouse_color = None
        satir.out_mouse_color = None
        satir.margins = [0,0]
        code_line_buttons.append(satir)
        




clock = pygame.time.Clock()
PLAY = True
filename_entry = entry.entry(150,0)
filename_entry.string = "example.txt"
filename_label = text.text.print_text("file name:")
oku_btn = button.button("dosya oku",300,0,200)
yukari_btn = button.button("^",500,0,50)
asagi_btn = button.button("v",500,50,50)
ileri_btn = button.button(">",500,100,50)
run_until_bp_btn = button.button(">|",500,150,50)
run_btn = button.button(">>>",500,200,50)


file_content = None
code_lines = []
code_line_buttons = []
bias1 = 0 
bias2 = 0
imlec = text.text.print_text("->")
imlec_satiri = 0
onceki_pc = 0
run = False
run_until_bp = False
break_points = []
registers_son_satir = 0
ssdisplay = ss_display.display([300,300])



def execute_one_step():
    pc = registers['pc']
    registers['pc']+=1
    execute_op.execute(code_lines[pc],registers,stack,memory)


while PLAY:

    pencere.fill((0,0,0))

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        filename_entry.update(event)
    
    pencere.blit(filename_label,(0,0))
    filename_entry.draw(pencere)
    oku_btn.draw(pencere)
    asagi_btn.draw(pencere)
    yukari_btn.draw(pencere)
    ileri_btn.draw(pencere)
    run_btn.draw(pencere)
    run_until_bp_btn.draw(pencere)
    
    pencere.blit(imlec,(550,bias1+bias2+registers["pc"]*25))

    led_values = bin((registers['&p1dir'] %256+256) & (registers['&p1out'] %256 + 256))
    #print("leds:",led_values)
    for i in range(8):
        color = (255,0,0) if led_values[i+3] == '1' else (75,0,0)
        pygame.draw.circle(pencere,color,(100,300+i*50),20)

    led_values = bin((registers['&p2dir'] %256+256) & (registers['&p2out'] %256 + 256))
    for i in range(8):
        color = (255,0,0) if led_values[i+3] == '1' else (75,0,0)
        pygame.draw.circle(pencere,color,(200,300+i*50),20)

    ssdisp_val = bin(registers["&p1out"]%256+256)[3:]
    ssdisplay.draw(pencere,ssdisp_val)

    if asagi_btn.is_click():
        bias1-=25
        get_code_line_buttons()
        
    if yukari_btn.is_click():
        bias1+=25
        get_code_line_buttons()

    for i in range(len(code_line_buttons)):
        code_line_buttons[i].draw(pencere)
        if code_line_buttons[i].is_click():
            if i in break_points:
                break_points.remove(i)
            else:
                break_points.append(i)
    
    
    

    

    for i in break_points:
        pygame.draw.circle(pencere,(255,0,255),(590,i*25+bias1+bias2+10),10)
    
    for i in range(len(registers)):
        key = list(registers.keys())[i]
        yazi = text.text.print_text(key+': '+str(registers[key]))
        pencere.blit(yazi,(1000,i*25))
        registers_son_satir = i*25
    
    for i in range(len(stack)+1):
        if i == len(stack):
            yazi = text.text.print_text('Stack content')
            pencere.blit(yazi,(1000,50+registers_son_satir))

        else:
            
            yazi = text.text.print_text(str(stack[-1+i]),yazi_rengi= ((0,255,0) if i == 0 else (255,255,255) ))
        
            pencere.blit(yazi,(1000,i*25+75+registers_son_satir))



    pencere.blit(text.text.print_text("Memory content:"),(1200,0))
    for i in range(len(memory)):
            yazi = text.text.print_text(str(i)+")"+str(memory[i]))
            pencere.blit(yazi,(1200,i*25+25))

    

    

    if oku_btn.is_click():
        filename = filename_entry.string
        dosya = open(filename,"r")
        file_content = dosya.readlines()
        dosya.close()
        code_lines = execute_op.convert_execution_list(file_content)
        print(code_lines)

        is_last_element = False 
        for i in range(len(code_lines)):
            if is_last_element:
                is_last_element = False
                continue
            if execute_op.find_labels(code_lines,i,memory) == "last_element":
                is_last_element = True
        get_code_line_buttons()

    if ileri_btn.is_click():

        if registers['pc']<len(code_lines):
            execute_one_step()
        if abs(onceki_pc-registers['pc']) > 1:
            bias2 = -registers['pc']*25
            get_code_line_buttons()
        onceki_pc = registers['pc']
    
    if run_btn.is_click():
        if run == False:
            run = True
            run_btn.update_string("| |")
        elif run == True:
            run = False
            run_btn.update_string(">>>")
        
    
    if run:
        if registers['pc']<len(code_lines):
            execute_one_step()
        if abs(onceki_pc-registers['pc']) > 1:
            bias2 = -registers['pc']*25
            get_code_line_buttons()
        onceki_pc = registers['pc']

    if run_until_bp_btn.is_click():
        run_until_bp = True
    
    if run_until_bp == True:
        if registers['pc']<len(code_lines):
            execute_one_step()
        if abs(onceki_pc-registers['pc']) > 1:
            bias2 = -registers['pc']*25
            get_code_line_buttons()
        onceki_pc = registers['pc']
        if registers['pc'] in break_points:
            run_until_bp = False
    
    
    






        print(registers)
        print(stack)

    pygame.display.update()

