{pkgs ? import <nixpkgs> {}}:
pkgs.mkShell {
  buildInputs = with pkgs; [
    python3Packages.streamlit
    python3Packages.pyperclip
    python3Packages.pytesseract
    tesseract
  ];
  shellHook = ''
    # exported variables maybe...
  '';
}
