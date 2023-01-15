import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class ServerDocSo {
    public static void main(String[] args){
        try{
            ServerSocket ss = new ServerSocket(7000);
            System.out.println("Da khoi tao xong Server cong 7000");
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
                    switch(ch) {
                        case '0' : ketqua = "Khong"; break;
                        case '1' : ketqua = "Mot"; break;
                        case '2' : ketqua = "Hai"; break;
                        case '3' : ketqua = "Ba"; break;
                        case '4' : ketqua = "Bon"; break;
                        case '5' : ketqua = "Nam"; break;
                        case '6' : ketqua = "Sau"; break;
                        case '7' : ketqua = "Bay"; break;
                        case '8' : ketqua = "Tam"; break;
                        case '9' : ketqua = "Chin"; break;
                    }
                    byte b[] = ketqua.getBytes();
                    os.write(b);
                }
                System.out.println("--Dong ket noi voi 1 Client");
                s.close();
            }
        }
        catch (IOException e) {
            System.out.println("Loi nhap xuat");
        }
    }
}
