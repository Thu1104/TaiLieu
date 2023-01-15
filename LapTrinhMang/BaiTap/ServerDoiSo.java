import java.io.InputStream;
import java.net.ServerSocket;

public class ServerDoiSo {
    public static void main(String[] args) {
        try{
            ServerSocket ss = new ServerSocket(3000);
            System.out.println("Da khoi ta xong server cong 3000");
            while(true){
                Socket s = ss.accept();
                System.out.println("Co 1 client " + s.getInetAddress() + " cong " + s.getPort() + " noi ket");
                InputStream is = s.getInputStream();
                OutputStream os = s.getOutputStream();
                while(true){
                    int ch = is.read();
                    System.out.println("Nhan tu client: " + ch);
                    if(ch == '@') break;
                    String ketqua = "Khong biet";
                    
                }
            }
        }
    }
    
}
