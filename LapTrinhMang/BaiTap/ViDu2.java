import java.io.FileInputStream;
import java.util.Scanner;
import java.io.*;
class DocFileText1 {
    public static void main(String[] args) {
        try {
            //Nhap ten file can doc
            Scanner kb = new Scanner(System.in);
            System.out.print("Nhap ten file can doc: ");
            String tenfile = kb.nextLine();
            //Mo file
            FileInputStream f = new FileInputStream(tenfile);
            //Doc noi dung 1 file text
            System.out.println("Noi dung file la:");
            while (true) {
                int ch = f.read();
                if (ch == -1)
                    break;
                System.out.print((char)ch);
            }
            f.close();
        } catch (FileNotFoundException e) {
            System.out.println("Khong tin thay file yeu cau");
        }
        catch (IOException e) {
            System.out.println("Loi nhap xuat");
        }
    }
}
