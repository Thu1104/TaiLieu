
namespace Bai_5
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.btnBT4 = new System.Windows.Forms.Button();
            this.btnThoat = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // btnBT4
            // 
            this.btnBT4.Location = new System.Drawing.Point(128, 84);
            this.btnBT4.Name = "btnBT4";
            this.btnBT4.Size = new System.Drawing.Size(75, 23);
            this.btnBT4.TabIndex = 0;
            this.btnBT4.Text = "Bài tập 4";
            this.btnBT4.UseVisualStyleBackColor = true;
            this.btnBT4.Click += new System.EventHandler(this.btnBT4_Click);
            // 
            // btnThoat
            // 
            this.btnThoat.Location = new System.Drawing.Point(280, 84);
            this.btnThoat.Name = "btnThoat";
            this.btnThoat.Size = new System.Drawing.Size(75, 23);
            this.btnThoat.TabIndex = 1;
            this.btnThoat.Text = "Thoát";
            this.btnThoat.UseVisualStyleBackColor = true;
            this.btnThoat.Click += new System.EventHandler(this.btnThoat_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 14F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(599, 266);
            this.Controls.Add(this.btnThoat);
            this.Controls.Add(this.btnBT4);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btnBT4;
        private System.Windows.Forms.Button btnThoat;
    }
}

