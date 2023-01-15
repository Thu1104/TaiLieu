import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class EchoServer {
    public static void main(String[] args) {
        try{
            //Khởi tạo server cổng 7
            ServerSocket ss = new ServerSocket(7);
            System.out.println("Da khoi tao xong server cong 7");
            while(true){
                //Chấp nhận cho nối kết
                Socket s = ss.accept();
                System.out.println("Co 1 Client " + s.getInetAddress() + " cong " + s.getPort() + " noi ket");
                //Lấy ra 2 stream in-out
                InputStream is = s.getInputStream();
                OutputStream os = s.getOutputStream();
                while(true){ //Phục vụ cho 1 client nhiều lần
                    //Nhận yêu cầu từ client (1 ký tự ch)
                    int ch = is.read();
                    System.out.println("Nhan tu Client: " + ch);
                    //Kiểm tra điều kiện để thoát
                    if(ch == '@') break;
                    //Xử lý yêu cầu
                    int ch1 = ch;
                    //Gửi kết quả cho Client
                    os.write(ch1);
                }
                //Đóng nối kết
                System.out.println("--Dong noi ket voi 1 client");
                s.close();
            }
        }
        catch (IOException e) {
            System.out.println("Loi nhap xuat!");
        }
    }
    
}
