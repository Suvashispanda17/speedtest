import speedtest 
st = speedtest.Speedtest() 

op=int(input("enter  the choice (1 ==== 2  =====  3 :  "))
if op == 1 :
    p= st.download()/1000000
    print(f"download  is {p:.2f}")
elif op == 2:
    z= st.upload()/1000000
    print(f"upload is {z:.2f}")
elif op == 3:
   
   servernames =[]   
   st.get_servers(servernames)   
   print(st.results.ping) 
else:
    print("invalid choice")
