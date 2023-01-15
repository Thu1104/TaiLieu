import java.io.*;
import java.net.*;
public class EchoHihi {
    public static void main(String[] args) {
        //Khởi tạo server cổng 7
        ServerSocket ss = new ServerSocket(7);
        System.out.println("Đã khởi tạo xong server cổng 7!");
        while(true){
            //Chấp nhận cho nối kết
            Socket s = ss.accept();
            System.out.println("Có 1 Client " + s.getInetAddress() + " cổng " + s.getPort() + " nối kết");
            //Lấy ra 2 stream in-out
            InputStream in = s.getInputStream();
            OutputStream os = s.getOutputStream();
            while(true){ //Phục vụ cho 1 client nhiều lần
                //Nhận yêu cầu từ client (1 ký tự ch)
                int ch = is.real();
                System.out.println("Nhận từ Client: " + ch);
                //Kiểm tra điều kiện để thoát
                if(ch == "@") break;
                //Xử lý yêu cầu
                int ch1 = ch;
                //Gửi kết quả cho Client
                os.write(ch1);
            }
            //Đóng nối kết
            System.out.println("--Đóng nối kết với 1 client");
            s.close();
        }
    }
    
}
