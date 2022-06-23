package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;


public class maina extends Application {
	
	TextField tf1;
	TextField tf2;
	TextField tf3;
	TextField tf4;
	
	@Override
	public void start(Stage primaryStage) {
		try {
			VBox root = (VBox)FXMLLoader.load(getClass().getResource("maina.fxml"));

			Scene scene = new Scene(root,400,400);
			
			tf1 = (TextField) scene.lookup("#tf1");
			tf2 = (TextField) scene.lookup("#tf2");
			tf3 = (TextField) scene.lookup("#tf3");
			tf4 = (TextField) scene.lookup("#tf4");
			
			Button btn = (Button) scene.lookup("#배수의합은");
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myclick();
				}	
			});
			
			
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public void myclick() {
		int a = Integer.parseInt(tf1.getText());
		int b = Integer.parseInt(tf2.getText());
		int c = Integer.parseInt(tf3.getText());
		String result = "";
		
		for(int i=a; i<=b; i++) {
			if(i%c == 0) {
				result += (i+" ");
			}
		}
		tf4.setText(result);
	}
	
	
	public static void main(String[] args) {
		launch(args);
	}
}
