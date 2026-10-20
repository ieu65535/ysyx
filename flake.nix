{
  description = "my Nix-flake-based ysyx learning environment";

  inputs.nixpkgs.url = "git+ssh://git@github.com/NixOS/nixpkgs.git?ref=nixos-unstable&shallow=1";

  outputs =
    { self, ... }@inputs:

    let
      inherit (inputs.nixpkgs.lib) genAttrs;
      supportedSystems = [
        "x86_64-linux"
        "aarch64-linux"
        "aarch64-darwin"
      ];
      forEachSystem =
        f:
        genAttrs supportedSystems (
          system:
          f {
            inherit system;
            pkgs = import inputs.nixpkgs { inherit system; };
          }
        );
    in
    {
      devShells = forEachSystem (
        { pkgs, system }:
        let
          python = pkgs.python3.withPackages (pkgs: with pkgs; [
          ]);
        in
        {
          default = pkgs.mkShell
          {
            packages = with pkgs; [
              python
              logisim
            ];
          };
        }
      );
    };
}
