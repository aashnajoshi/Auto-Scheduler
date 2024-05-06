_name__ == "__main__":
    initialize(data)
    T_T_G(classes.keys())
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())