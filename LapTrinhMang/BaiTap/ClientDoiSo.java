import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;

public class ClientDoiSo {
    public static void main(String[] args) {
        try{
            Socket s = new Socket("127.0.0.1", 3000);
            InputStream is = s.getInputStream();
            OutputStream os = s.getOutputStream();
            while(true){
                System.out.print("Nhap mot so: ");
                int ch = System.in.read();
                os.write(ch);
                System.in.skip(2);
                if(ch == '@') break;
                byte b[] = new byte[1000];
                int n = is.read(b);
                String ketqua = new String(b, 0, n);
                System.out.println("Gia tri nhi phan cua " + n + " la: " + ketqua);
            }
            s.close();
        }
        catch (IOException e) {
            System.out.println(e);
        }
    }
}
