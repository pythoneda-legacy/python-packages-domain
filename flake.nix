{
  description = "The domain of Python packages in the common ecosystem";

  inputs = rec {
    nixos.url = "github:NixOS/nixpkgs/nixos-22.11";
    flake-utils.url = "github:numtide/flake-utils";
    pythoneda.url = "github:rydnr/pythoneda";
    ecosystem_nix_shared.url = "github:rydnr/ecosystem-nix-shared";
    ecosystem_git_repositories.url = "github:rydnr/ecosystem-git-repositories";
    poetry2nix = {
      url = "github:nix-community/poetry2nix";
      inputs.nixpkgs.follows = "nixos";
      inputs.flake-utils.follows = "flake-utils";
      inputs.pythoneda.follows = "nixos";
      inputs.ecosystem_git_repositories.follows = "nixos";
      inputs.ecosystem_nix_shared.follows = "nixos";
    };
  };
  outputs = inputs:
    with inputs;
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixos { inherit system; };
        python = pkgs.python3;
        pythonPackages = python.pkgs;
        inherit (poetry2nix.legacyPackages.${system}) mkPoetryApplication;
        description = "The domain of Python packages in the common ecosystem";
        license = pkgs.lib.licenses.gpl3;
        maintainers = with pkgs.lib.maintainers; [ ];
      in rec {
        packages = {
          ecosystem_python_packages = mkPoetryApplication rec {
            pname = "ecosystem_python_packages";
            version = "0.0.alpha.1";
            format = "pyproject";
            projectDir = ./.;

            propagatedBuildInputs = with pythonPackages; [
              pythoneda
              ecosystem_nix_shared
              ecosystem_git_repositories
            ];
            pythonImportsCheck = [ ];

            meta = with pkgs.lib; {
              inherit description license homepage maintainers;
            };
          };
          default = packages.ecosystem_python_packages;
          meta = with lib; {
            inherit description license homepage maintainers;
          };
        };
        defaultPackage = packages.default;
        devShell = pkgs.mkShell {
          buildInputs = with pkgs.python3Packages; [ packages.default ];
        };
        shell = flake-utils.lib.mkShell {
          packages = system: [ self.packages.${system}.default ];
        };
      });
}
