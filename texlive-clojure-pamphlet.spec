Name:		texlive-clojure-pamphlet
Version:	60981
Release:	2
Summary:	A simple literate programming tool based on clojure's pamphlet system
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/clojure-pamphlet
License:	gpl3+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clojure-pamphlet.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clojure-pamphlet.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clojure-pamphlet.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Clojure pamphlet system is a system based on the Clojure
literate system. In the Clojure's pamphlet system you have your
main LaTeX file, which can be compiled regularly. This file
contains documentation and source code (just like in other
forms of literate programming). These code snippets are wrapped
in the chunk environment, hence they can be recognized by the
tangler in order to extract them. Chunks can be included inside
each other by the getchunk command (which will be typesetted
acordingly). Finally, the LaTeX file will be run through the
tangler to get the desired chunk of code.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%doc %{_texmfdistdir}/texmf-dist/source/support/clojure-pamphlet
%{_texmfdistdir}/texmf-dist/tex/latex/clojure-pamphlet
%{_texmfdistdir}/texmf-dist/scripts/clojure-pamphlet
%doc %{_texmfdistdir}/texmf-dist/doc/support/clojure-pamphlet
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/pamphletangler.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/pamphletangler.1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
