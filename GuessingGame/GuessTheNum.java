/*  */
package GuessingGame;
import java.awt.Color;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.util.Scanner;

import javax.swing.AbstractAction;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;

public class GuessTheNum {
	public static JFrame frame;
	public static JPanel panel;
	public static JLabel guessNum;
	public static JTextField guessNumFrame;
	public static int guessAmount = 10;
	public static JLabel highOrLow;
	public static JButton submitGuess;
	public static Color correctColor = new Color(36, 163, 80);
	public static final int random = (int) (Math.random() * 100) + 1;
	public static JLabel guessAmountDisplay;
	public static JLabel guessAmountNum;
	public static JLabel numZero = new JLabel("0");
	public static JLabel scoreDisplay;
	public static JLabel scoreNum;
	public static int score = 100;
	public static JButton replayButton;
		
		public static void main(String arg[]) {
			Scanner s = new Scanner(System.in);
			frame = new JFrame();
			frame.setSize(500,300);
			frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			panel = new JPanel();
			panel.setLayout(null);
			frame.add(panel);
			

				guessNum = new JLabel("Guess The Number (Between 1 and 100)");
				guessNum.setBounds(115, 20, 350, 60);
				guessNum.setFont(new Font("Calibri", Font.PLAIN, 15 ));
				panel.add(guessNum);
				guessNumFrame = new JTextField();
				guessNumFrame.setBounds(150, 60, 200, 25);
				panel.add(guessNumFrame);
				highOrLow = new JLabel();
				highOrLow.setBounds(190, 90, 400, 30);
				panel.add(highOrLow);
				guessAmountDisplay = new JLabel("Remaing Guesses:");
				panel.add(guessAmountDisplay);
				guessAmountDisplay.setBounds(20, 13, 115, 30);
				guessAmountDisplay.setFont(new Font("Calibri", Font.PLAIN, 13));
				guessAmountNum = new JLabel(Integer.toString(guessAmount));
				panel.add(guessAmountNum);
				guessAmountNum.setBounds(23, 10, 100, 100);
				guessAmountNum.setFont(new Font("Calibri", Font.BOLD, 30));
				scoreDisplay = new JLabel("Score:");
				panel.add(scoreDisplay);
				scoreDisplay.setBounds(425, 13, 115, 30);
				scoreDisplay.setFont(new Font("Calibri", Font.PLAIN, 13));
				scoreNum = new JLabel(Integer.toString(score));
				panel.add(scoreNum);
				scoreNum.setBounds(423, 10, 100, 100);
				scoreNum.setFont(new Font("Calibri", Font.BOLD, 30));
				submitGuess = new JButton(new AbstractAction("Submit Guess") {

					public void actionPerformed(ActionEvent e) {	
						if(guessAmount >= 0) {
							int num = Integer.parseInt(guessNumFrame.getText().trim());
							if (guessAmount == 4) {
								guessAmountNum.setForeground(Color.RED);
							}
						if (num == random) {
								highOrLow.setText("You guessed the correct number!");
								s.close();
								highOrLow.setBounds(145, 80, 400, 30);
								highOrLow.setForeground(correctColor);
								panel.remove(guessNumFrame);
								panel.remove(guessAmountDisplay);
								panel.remove(guessAmountNum);
								panel.remove(submitGuess);
								panel.add(replayButton);
								panel.repaint();
							}
						if (guessAmount == 1) {
								highOrLow.setText("You have ran out of guesses. Game Over.");
								s.close();
								highOrLow.setBounds(125, 80, 450, 30);
								highOrLow.setForeground(Color.RED);
								guessAmountNum.setForeground(Color.RED);
								panel.remove(guessNumFrame);
								panel.remove(guessAmountNum);
								panel.add(numZero);
								numZero.setForeground(Color.RED);
								numZero.setBounds(23, 10, 100, 100);
								numZero.setFont(new Font("Calibri", Font.BOLD, 30));
								score-=10;
								scoreNum.setText(Integer.toString(score));
								panel.remove(submitGuess);
								panel.add(replayButton);
								panel.repaint();
								}
							
						
							else if (num < random) {
							highOrLow.setText("The number you entered is less than the generated number.");
							highOrLow.setBounds(75, 80, 450, 30);
							highOrLow.setForeground(Color.RED);
							guessAmount--;
							guessAmountNum.setText(Integer.toString(guessAmount));
							score-=10;
							scoreNum.setText(Integer.toString(score));
							panel.repaint();
						}
						else if (num > random) {
							highOrLow.setText("The number you entered is higher than the generated number.");
							highOrLow.setBounds(75, 80, 450, 30);
							highOrLow.setForeground(Color.RED);
							guessAmount--;
							guessAmountNum.setText(Integer.toString(guessAmount));
							score-=10;
							scoreNum.setText(Integer.toString(score));
							panel.repaint();
						}
						
						
						}
					
					
				}
				});
				submitGuess.setBounds(175, 120, 150, 30);
				panel.add(submitGuess);

			
			
			frame.setVisible(true);
		

	}
}