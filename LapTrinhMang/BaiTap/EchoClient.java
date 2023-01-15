import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;
import java.net.UnknownHostException;

public class EchoClient {
    public static void main(String[] args) {
        try{
            //Nối kết đến Server cổng 7
            Socket s = new Socket("127.0.0.1", 7);
            //Lấy ra 2 stream in- out
            InputStream is = s.getInputStream();
            OutputStream os = s.getOutputStream();
            while(true){
                //Nhập 1 ký tự từ bàn phím
                System.out.print("Nhap 1 ky tu: ");
                int ch = System.in.read();
                //Gửi ch qua Server
                os.write(ch);
                //Bỏ 2 ký tự dư thừa
                System.in.skip(2);
                //Kiểm tra điều kiện để thoát
                if(ch == '@') break;
                //Nhận kết quả trả về từ server
                int ch1 = is.read();
                //Hiển thị kết quả ra màn hình
                System.out.println("Nhan duoc: " + (char)ch1);
            }
            //Đóng nối kết
            s.close();
        }
        catch (UnknownHostException e) {
            System.out.println("Sai dia chi Server");
        }
        catch (IOException e) {
            System.out.println(e);
        }
    }
}
