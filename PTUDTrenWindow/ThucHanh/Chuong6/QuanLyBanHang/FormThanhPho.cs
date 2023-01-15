using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.SqlClient;

namespace QuanLyBanHang
{
    public partial class FormThanhPho : Form
    {
        string strConnectionString = @"Data Source=.\SQLEXPRESS;Initial Catalog=QuanLyBanHang;Integrated Security = True";
        SqlConnection conn = null;
        SqlDataAdapter daThanhPho = null;
        DataTable dtThanhPho = null;
        public FormThanhPho()
        {
            InitializeComponent();
        }

        private void FormThanhPho_Load(object sender, EventArgs e)
        {
            try
            {
                // Khởi động connection
                conn = new SqlConnection(strConnectionString);
                // Vận chuyển dữ liệu lên DataTable dtThanhPho
                daThanhPho = new SqlDataAdapter("SELECT * FROM THANHPHO", conn);
                dtThanhPho = new DataTable();
                dtThanhPho.Clear();
                daThanhPho.Fill(dtThanhPho);
                // Đưa dữ liệu lên ListBox
                this.lstThanhPho.DataSource = dtThanhPho;
                this.lstThanhPho.DisplayMember = "TenThanhPho";
                this.lstThanhPho.ValueMember = "ThanhPho";
            }
            catch (SqlException)
            {
                MessageBox.Show("Không lấy được nội dung trong table THANHPHO.Lỗi rồi!!!");
            }

        }

        private void FormThanhPho_FormClosing(object sender, FormClosingEventArgs e)
        {
            dtThanhPho.Dispose();
            dtThanhPho = null;
            conn = null;
        }

        private void btnThoat_Click(object sender, EventArgs e)
        {
            DialogResult traloi;
            traloi = MessageBox.Show("Chắc không?", "Trả lời", MessageBoxButtons.OKCancel, MessageBoxIcon.Question);
            if (traloi == DialogResult.OK) Application.Exit();
        }
    }
}
