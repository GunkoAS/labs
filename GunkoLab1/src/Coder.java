import java.io.*;
import java.util.Scanner;

public class Coder {
    public static String caesar(String text, int shift) {
        shift %= 33;
        if (shift == 0) return text;
        StringBuilder sb = new StringBuilder(text.length());
        for (int i = 0; i < text.length(); i++) {
            int c = text.charAt(i);

            if (c >= 'А' && c <= 'Я') {
                c += shift;
                if (c > 'Я') c -= 33;
            } else if (c >= 'а' && c <= 'я') {
                c += shift;
                if (c > 'я') c -= 33;
            }

            sb.append((char) c);
        }
        return sb.toString();
    }

    public static String decipher(String text, int shift) {
        shift %= 33;
        if (shift == 0) return text;
        StringBuilder sb = new StringBuilder(text.length());
        for (int i = 0; i < text.length(); i++) {
            int c = text.charAt(i);

            if (c >= 'А' && c <= 'Я') {
                c -= shift;
                //if (c > 'Я') c -= 33;
            } else if (c >= 'а' && c <= 'я') {
                c -= shift;
                //if (c > 'я') c -= 33;
            }

            sb.append((char) c);
        }
        return sb.toString();
    }

    //        try {
//            File newFile = new File("stalker(coded).txt");
//            newFile.createNewFile();
//            FileWriter writer = new FileWriter("stalker(coded).txt");
//            FileReader reader = new FileReader("stalker(src).txt");
//            int c;
//            while ((c=reader.read())!=-1) {
//                if ((c >= 1040 && c< 1070) || (c > 1071 && c < 1102)) writer.write((char)(c+2));
//                else switch (c) {
//                    case ((char)1070): writer.write('А'); break; //Э
//                    case ((char)1071): writer.write('Б'); break; //э
//                    case ((char)1102): writer.write('а'); break; //Я
//                    case ((char)1103): writer.write('б'); break; //я
//                    case ((char)1025): writer.write('З'); break; //Ё
//                    case ((char)1105): writer.write('з'); break; //ё
//                    default: writer.write((char)c); break;
//                }
//            }
//            writer.close();
//            reader.close();
//        }
//        catch(IOException e) {
//            System.out.println(e.getMessage());
//        }
    public static void main(String[] args) throws IOException {
        int shift = 1;
        try (Scanner input = new Scanner(new File("stalker(src).txt"));
             PrintStream output = new PrintStream(new File("stalker(coded).txt"))) {
            while (input.hasNextLine()) {
                output.println(caesar(input.nextLine(), shift));
            }
        }
    }
}



