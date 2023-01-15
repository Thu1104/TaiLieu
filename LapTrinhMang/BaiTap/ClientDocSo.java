import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;
import java.net.UnknownHostException;

public class ClientDocSo {
    public static void main(String[] args) {
        try {
            Socket s = new Socket("127.0.0.1", 7000);
            InputStream is = s.getInputStream();
            OutputStream os = s.getOutputStream();
            while (true) {
                System.out.print("Nhap 1 ky tu (0-9): ");
                int ch = System.in.read();
                os.write(ch);
                System.in.skip(2);
                if (ch == '@')
                    break;
                byte b[] = new byte[1000];
                int n = is.read(b);
                String ketqua = new String(b, 0, n);
                System.out.println("Ket qua la: " + ketqua);
            }
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
